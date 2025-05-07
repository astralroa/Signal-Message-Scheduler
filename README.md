Hello there! Signal Message Scheduler is a simple python script that is designed to help you schedule you messages on signal PC Version. (Recommended to run on servers)
THis tool uses signal CLI in order to schedule messages on the machine that it is being run on.

<h1>INSTALLATION</h1>

Step 1: Install signal-cli.

```sudo apt install signal-cli```

HELP! If signal-cli is not in your default packages, you can install it manually.
```wget https://github.com/AsamK/signal-cli/releases/latest/download/signal-cli-linux.tar.gz```

This will install the latest version of signal-cli on your machine via wget

Extcract the provided archive:
```tar -xvf signal-cli-linux.tar.gz```

Move signal-cli to a system directory:

```sudo mv signal-cli-*/bin/signal-cli /usr/local/bin/```

Verify Installation:
```signal-cli --version```

Step 2: Link signal-cli to your signal account.

```signal-cli link```

Step 3: Ensure that you have the packages for the python script installed.

```sudo apt install python3-tk```

Step 4: Lastly, Run the python file that is provided and Schedule your first message!

```python3 signals.py```
