def http_status(status):
    match status:
        case 200:
            return "ok"
        case 300:
            return "unknown"
        case 500: 
            return "invalid"
        case _:
            return "unknown status"
print(http_status(550)) 




#merged dictionary
dic={
    "a":3

} 
dic2={
    'b':4

}
merged=dic|dic2
print(merged)