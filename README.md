<h3>Hello there! Signal Message Scheduler is a simple python script that is designed to help you schedule you messages on signal PC Version. (Recommended to run on servers)</h3>
<h3></h3>This tool uses signal CLI in order to schedule messages on the machine that it is being run on.</h3>

<h1>INSTALLATION</h1>

<h2>Step 1: Install signal-cli.</h2>

```sudo apt install signal-cli```

<h2>HELP! If signal-cli is not in your default packages, you can install it manually.</h2>

```wget https://github.com/AsamK/signal-cli/releases/latest/download/signal-cli-linux.tar.gz```

<h2>This will install the latest version of signal-cli on your machine via wget</h2>

<h2>Extcract the provided archive:</h2>

```tar -xvf signal-cli-linux.tar.gz```

<h2>Move signal-cli to a system directory:</h2>

```sudo mv signal-cli-*/bin/signal-cli /usr/local/bin/```

<h2>Verify Installation:</h2>

```signal-cli --version```

<h2>Step 2: Link signal-cli to your signal account.</h2>

```signal-cli link```

<h2>Step 3: Ensure that you have the packages for the python script installed.</h2>

```sudo apt install python3-tk```

<h2>Step 4: Lastly, Run the python file that is provided and Schedule your first message!</h2>

```python3 signals.py```
