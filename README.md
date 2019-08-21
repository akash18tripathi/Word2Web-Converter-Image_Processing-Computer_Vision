# Word2Web-Converter-Image_Processing-Computer_Vision
This Project can convert a handwritten word to a webpage element by training a CNN model on the words manually and integrating it with Flask Web server

## Installation

```bash
pip install opencv-python
```
```bash
pip install gevent
```
```bash
pip install Flask
```
## Steps for running this Project:
1)Install the dependencies mentioned above.

2)Run word2web_converter.py and open http://localhost:5000 to directly get the results.

3)You can run the generate_data.py , where you have to manually write each word("HEAD","NAV","MAIN") 80 times.

4)After generating data, running trainer.py will train the generated images on Convolutional neural network and generate model.h5 file.

5)Finally run word2web_converter.py and open http://localhost:5000 to directly get the results.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Any suggestions regarding the extensions of this simple project are most welcome!.

## Final Result- Drawing Tool
![](word2web.gif)
