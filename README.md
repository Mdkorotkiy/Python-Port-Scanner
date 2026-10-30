***Python Port Scanner***



A Python-based TCP port scanner designed to identify open ports and their commonly associated network services.



**Features**



* TCP port scanning (ports 1–1024)
* Open port detection
* Common service identification
* Hostname resolution
* Scan duration tracking
* Error handling
* ASCII banner



**Technologies Used**



* Python 3
* Socket Programming
* PyFiglet
* TCP/IP Networking



**Installation**



Install the required dependencies:



**python -m pip install -r requirements.txt**



**Usage**



Scan your local computer:



*python scanner.py 127.0.0.1*



**Example Output**



PORT        STATE       SERVICE

135         OPEN        epmap

445         OPEN        microsoft-ds



Total open ports: 2



**Future Improvements**

* Multithreaded scanning
* Custom port ranges
* Service banner detection
* Export results to CSV
* Graphical user interface

