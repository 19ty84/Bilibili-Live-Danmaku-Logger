# This is the older version of [Bilibili-Live-Danmaku-Logger-V2](https://github.com/19ty84/Bilibili-Live-Danmaku-Logger-V2)
To create log files in .csv format and logging emoticons, please visit [Bilibili-Live-Danmaku-Logger-V2](https://github.com/19ty84/Bilibili-Live-Danmaku-Logger-V2).

------------

# Bilibili-Live-Danmaku-Logger
Gets and logs danmaku from a Bilibili live room.

## How to use

### config.txt 

Before running the program, first configure the `config.txt` file. `config.txt` looks like:

```
room_id = 1779910052
log_file_create_interval = 3600
log_file_save_interval = 60
request_interval = 3
```

`room_id`: Int. The room ID of your target Bilibili live room. For example, if the link is `https://live.bilibili.com/1779910052`, then the room ID is 1779910052.

`log_file_create_interval`: Float. Number of seconds between creating new log files. It can be set to `inf` so that the program only creates one log file.

`log_file_save_interval`: Float. Number of seconds between saving current log file.

`request_interval`: Float. Number of seconds between two requests. If there are a lot of danmaku in a short time, request interval should be smaller, or it would miss some danmaku.

### Run the program

```
python logger.py
```

The first logs will be logged and printed at `request_interval` seconds after the program starts.

## Logs

Logs will be under `log/` directory. If the directory doesn't exist, the program will generate it.

Log files are named as `danmaku{time}.log`. A log file named `danmaku1772302358.log` means the log starts at time 1772302358.
