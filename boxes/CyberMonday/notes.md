
It looks like I can enumerate users using `curl`. i.e. a user named "admin" already exists.

    curl "http://cybermonday.htb/signup" \
    -X POST \
    -H 'upgrade-insecure-requests: 1' \
    -H 'cookie: XSRF-TOKEN=eyJpdiI6InQzNzZ2YU9IUHY3Y3RIMjJHTDhSMVE9PSIsInZhbHVlIjoiZ0IvR3BkSHVyZEF3REd0dU5KbnRVZ0xscUlJNklxNU5iQUhYSHlIZGd5L0dFQkxLZ2haTERRdTgwaEsyNEFzU0ovbGc2Ty9qUGFQZWsxV3hPTExFbHAySG5ZQW1hSDFYZHVsUW80ckRqVnBVa2R5Y2YvcFB6M3BXc1BMc2ZHNVIiLCJtYWMiOiIwNGNhZGEwNTQzNDM5OWU0M2EyZmQ0MzZiYzNmZDg3MzI3YmYwYTNkODk3OWM4ZTY3YjJmMTYzZDNlNTBhZTNkIiwidGFnIjoiIn0%3D; cybermonday_session=eyJpdiI6IkJsTGViRGFkbG84S3ZOTzJDcGdmaUE9PSIsInZhbHVlIjoicndKZ1lRV3JjV2xJdEVLS0QwQkZ3bnhzMTV0eWVKVm9naG51OWpRNWthcURTQnU0TFJhTHgvN05LWE9HNjNJbkNzek1TWWZkd3lBNXY2WkIwR0NRbnBlMlBKMWI4WjI0aDA1elJYUzQzcGcvWlpQcXU1YTc3QW1tNlpxOGJGYVciLCJtYWMiOiI3MWU2Y2ZjYTI3MWY1OGQyNzMyZmNhODhmNzYxMzRiZDdkMmUwZTBlNzkwNDY0YzY2ZmJjMGJjZjA5MTk1ZDFmIiwidGFnIjoiIn0%3D' \
    -H 'connection: keep-alive' \
    -H 'dnt: 1' \
    -H 'origin: http://cybermonday.htb' \
    -H 'content-length: 101' \
    -H 'content-type: application/x-www-form-urlencoded' \
    -H 'referer: http://cybermonday.htb/signup' \
    -H 'accept-encoding: gzip, deflate' \
    -H 'accept-language: en-US,en;q=0.5' \
    -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' \
    -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0' \
    -H 'host: cybermonday.htb' \
    -F '_token=3xrn4SrvnRkqCLWwZJxtGO1EFPjxrpwdWITQwOtu' -F 'username=admin' -F 'email=admin@gmail.com' -F 'password=admin'