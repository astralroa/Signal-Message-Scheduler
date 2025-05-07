<h3>Hello there! Signal Message Scheduler is a simple python script that is designed to help you schedule you messages on signal PC Version. (Recommended to run on servers)</h3>
<h3></h3>This tool uses signal CLI in order to schedule messages on the machine that it is being run on.</h3>

<h1>INSTALLATION</h1>

<h3>Step 1: Install signal-cli.</h3>

```sudo apt install signal-cli```

<h3>HELP! If signal-cli is not in your default packages, you can install it manually.</h3>

```wget https://github.com/AsamK/signal-cli/releases/latest/download/signal-cli-linux.tar.gz```

<h3>This will install the latest version of signal-cli on your machine via wget</h3>

<h3>Extcract the provided archive:</h3>

```tar -xvf signal-cli-linux.tar.gz```

<h3>Move signal-cli to a system directory:</h3>

```sudo mv signal-cli-*/bin/signal-cli /usr/local/bin/```

<h3>Verify Installation:</h3>

```signal-cli --version```

<h3>Step 2: Link signal-cli to your signal account.</h3>

```signal-cli link```

<h3>Step 3: Ensure that you have the packages for the python script installed.</h3>

```sudo apt install python3-tk```

<h3>Step 4: Lastly, Run the python file that is provided and Schedule your first message!</h3>

```python3 signals.py```


![Screenshot_2025-05-07_16_45_41](https://github.com/user-attachments/assets/5d9b580d-5fe7-4168-84b6-a6ca0da8bbf7)
