# Mission To Mars
## Purpose
The purpose of the following repository is to create a web app to scrape the web for recent and relevant information on the planet Mars. The information that the web app represents is: _Latest News_ on the red planet's situation, a  _Featured Photo_, _Mars Facts_ and images on _Hemispheres_; taken from different sites and compiled and presented in a single page for the enjoyment of those inquiring.

## Requirements
Please make sure you have installed the following components to successfully run the web app:

- [Python 3.7](https://www.python.org/downloads/) or greater
- [MongoDB](https://www.mongodb.com/en-us/pricing)

**Note:** Be sure to install any missing modules from ```app.py``` before running the required servers.

## How to scrape with the Mission To Mars web app
Simply click the ```Scrape New Data``` button and wait to see the web scraped and your information delivered

## How to run MongoDB server and web app
Before opening the web app, you need to initialize the Mongo and Flask servers
1. On the command line, activate your MongoDB server by typing ```mongod```.
2. Open a new command prompt and navigate to the project folder; initialize the web app by typing ```python app.py```.
3. On a web browser navigate to the [localhost server](https://127.0.0.1:5000) and start scraping!

## Sources
The sources we scraped from were the following:
- *Latest Mars News*: [Mars Planet Science Exploration Program](https://redplanetscience.com/)
- *Featured Photo*: [Jet Propulsion Laboratory](https://spaceimages-mars.com) from the California Institute of Technology
- *Mars Facts*: [Galaxy Facts](https://galaxyfacts-mars.com)
- *Hemisphere unformation*: [NASA's Astropedia](https://marshemispheres.com/)
