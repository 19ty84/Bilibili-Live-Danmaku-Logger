import time
import requests
import os

DEFAULT_ROOM_ID = 1779910052
DEFAULT_LOG_FILE_CREATE_INTERVAL = 3600
DEFAULT_LOG_FILE_SAVE_INTERVAL = 60
DEFAULT_REQUEST_INTERVAL = 3
DEFAULT_LOG_LIST_MAX_LENGTH = 200
DEFAULT_LOG_LIST_EXPECTED_LENGTH = 100

room_id = DEFAULT_ROOM_ID
log_file_create_interval = DEFAULT_LOG_FILE_CREATE_INTERVAL
log_file_save_interval = DEFAULT_LOG_FILE_SAVE_INTERVAL
request_interval = DEFAULT_REQUEST_INTERVAL
log_list_max_length = DEFAULT_LOG_LIST_MAX_LENGTH
log_list_expected_length = DEFAULT_LOG_LIST_MAX_LENGTH

# Read config file
config_file = open("./config.txt", mode="r", encoding="utf-8")
config = config_file.readlines()
config_file.close()
for str in config:
    try:
        key = str[: str.index("=")].strip()
        value = str[str.index("=") + 1 :].strip()
        if key == "room_id":
            room_id = int(value)
        elif key == "log_file_create_interval":
            log_file_create_interval = float(value)
        elif key == "log_file_save_interval":
            log_file_save_interval = float(value)
        elif key == "request_interval":
            request_interval = float(value)
        elif key == "log_list_max_length":
            log_list_max_length = int(value)
        elif key == "log_list_expected_length":
            log_list_expected_length = int(value)
    except:
        print("Error in config.txt:")
        print("String", str, "is not valid")
        raise

url = "https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory"
headers = {
    "Host": "api.live.bilibili.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
}
data = {"roomid": room_id}

nowtime = time.time()
log_create_time = nowtime
log_last_save_time = nowtime

# Open log file
try:
    os.mkdir("./logs")
except FileExistsError:
    pass
log_file_write = open(
    f"./logs/danmaku{int(log_create_time)}.log", mode="a", encoding="utf-8"
)
log_file_read = open(
    f"./logs/danmaku{int(log_create_time)}.log", mode="r", encoding="utf-8"
)
log_list = log_file_read.readlines()
log_file_read.close()

while 1:
    time.sleep(request_interval)

    nowtime = time.time()

    if len(log_list) > log_list_max_length:
        log_list = log_list[-log_list_expected_length:]  # Shorten the list

    if nowtime - log_create_time > log_file_create_interval:
        # Create new log file
        log_file_write.close()
        log_create_time = nowtime
        log_file_write = open(
            f"./logs/danmaku{int(log_create_time)}.log", mode="a", encoding="utf-8"
        )
    elif nowtime - log_last_save_time > log_file_save_interval:
        # Save log file
        log_file_write.close()
        log_file_write = open(
            f"./logs/danmaku{int(log_create_time)}.log", mode="a", encoding="utf-8"
        )
        log_last_save_time = nowtime

    # Get danmaku from live room
    try:
        response_json = requests.post(url=url, headers=headers, data=data).json()
    except:
        print(nowtime, "Failed to get danmaku")
        continue

    # Print and save danmaku
    for content in response_json["data"]["room"]:
        nickname = content["nickname"]
        text = content["text"]
        timeline = content["timeline"]
        msg = timeline + " " + nickname + ": " + text

        # Check if the message exist in log_list
        if msg in log_list:
            continue

        print(msg)
        log_file_write.write(msg + "\n")
        log_list.append(msg)
