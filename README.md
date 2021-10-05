
# LoanPaymentCalculator
in case that a folder called /tmp does not exist in your home directory create one, the logs will be added there. 
Navigate to the main directory of project LoanPaymentCalculator then execute the follow command to start the calculator:
```shell
pip install -r requirements.txt
python main.py
```
## Expected input
Expected a new line key press after every line from below lines.
```shell
amount:100000
interest:5.5%
downpayment:20000
term:30
```
It will calculate the a similar output based on the input:
```shell
{
  "monthly payment": 454.23,
  "total interest": 83523.23,
  "total payment": 163523.23
}

```
## Executing tests
```shell
pytest
```
## Contact
**email:** pablo5516@gmail.com
**Created By:** Juan Pablo Lopez Gutierrez
