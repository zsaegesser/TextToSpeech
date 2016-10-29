from gtts import gTTS
import urllib2

response = urllib2.urlopen('http://www.accuweather.com/en/us/jersey-city-nj/07306/weather-forecast/329548')
html = response.read()
#print html

found = html.find('class="local-temp"', 50000,70000)
temp = html[found+19:found+21]
statement = 'The current temperature is ' + temp + 'degrees'
tts = gTTS(text=statement, lang='en')
tts.save('temperature.mp3')
print(statement)
