#import flask library
from flask import Flask, render_template, request
import requests
#initialize flask
app = Flask(_name_)
#route your webpage
@app.route("/")
def visitors():

	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	# Increment the count
	visitors_count = visitors_count + 1

	# Overwrite the count
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()

# Render HTML with count variable
    return render_template("index.html", count = visitors_count)

#route your webpage
@app.route('/', methods = ['POST'])
def weather_stats():
	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	latitude = reqest.form['latitude']
	longitude = request.form['longitude']

	api_url = 'https://weather-l6tl.onrender.com/api/getCurrentWeather/' + latitude + '/' + longitude

	response = requests.get(api_url)
	weather_data = response.json()
	print(weather_data)
	return render_template("index.html", weather = weather_data, count = visitors_count)
	#complete the code

if _name_ == " __main__":
	app.run()
#add code for executing flask