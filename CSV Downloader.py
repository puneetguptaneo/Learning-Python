from urllib import request

file_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=8&e=3&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv"

def download_csv(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_csv(file_url)

