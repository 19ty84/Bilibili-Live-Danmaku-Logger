# Bilibili-Live-Danmaku-Logger
Gets and logs danmaku from a Bilibili live room.

## How to use

### config.txt 

Before running, first configure the config.txt file. Things in config.txt are like:

```
room_id = 1779910052
log_file_create_interval = 3600
log_file_save_interval = 60
request_interval = 3
```

`room_id`: Int. The room ID of your target Bilibili live room. For example, if the link is `https://live.bilibili.com/1779910052`, then the room ID is 1779910052.

`log_file_create_interval`: Float. Number of seconds between creating new log files.

`log_file_save_interval`: Float. Number of seconds between saving current log file.

`request_interval`: Float. Number of seconds between two requests. If there are a lot of danmaku in a short time, request interval should be smaller, or it would miss some danmaku.

### Run the program

```
python logger.py
```

## Logs

Logs will be under `log/` directory. If the directory doesn't exist, the program will generate it.

A log file named `danmaku1772302358.log` means the log starts from time 1772302358.
