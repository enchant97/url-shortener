# Url-Short
A simple way to shorten urls on a self-hosted server.
Designed to be fast and lightweight.
Using asyncio for everything possible.

> Please note this project is not fully tested and is a WIP.

## This Project Is EOL
What Does This Mean?
- No more updates
- This repo will be archived

Why?
- I have decided to make it using Go, called [url-shorter](https://github.com/enchant97/url-shorter)
    - A go implementation will allow for faster redirects

## Config
You can configure the app using a .env file or through environment variables.

| Name                   | Description                            | Required | Default            |
|:-----------------------|:-------------------------------------- |:---------|:-------------------|
| DB_URI                 | URI of where db is stored              | YES      |                    |
| LOG_LEVEL              | What log level to use                  | NO       | "WARNING"          |
| HOST                   | host to listen for requests            | NO       | "127.0.0.1"        |
| PORT                   | port to listen for requests            | NO       | 8000               |
| SERVER_NAME            | name of the server                     | NO       |                    |


## License
Copyright (C) 2021 Leo Spratt

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
