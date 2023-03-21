# IOL Invertironline API Project

This project is a Python application that consumes the IOL Invertironline REST API. The IOL Invertironline API provides access to financial market data and allows users to perform financial transactions in the Argentine market.

## Getting Started

To use this application, you will need a valid username and password for the IOL Invertironline platform. You will also need to obtain an access token from the API by following the instructions on the IOL Invertironline developer portal.

Once you have an access token, you can clone this repository to your local machine:

'''bash
git clone <https://github.com/ignacioNicolasAlvarez/iol-api-project.git>
'''

Next, create a virtual environment for the project and install the required dependencies:

'''bash
cd iol-api-project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
'''

Then, create a .secrets.toml file in the root directory of the project with the following contents:

'''bash
[iol.credentials]
username = "yourusername"
password = "yourpassword"
'''

Replace the values yourusername and yourpassword with your actual IOL Invertironline API credentials.

## Usage

The main functionality of this application is to retrieve a list of completed financial transactions (operaciones) from the IOL Invertironline API. You can customize the date range of the transactions using the fecha_desde and fecha_hasta parameters.

To run the application, execute the following command:

'''bash
python main.py
'''

## Contributing

If you would like to contribute to this project, feel free to submit a pull request. Before doing so, please make sure that your code follows the PEP 8 style guide and includes appropriate tests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
