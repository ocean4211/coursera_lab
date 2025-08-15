There are scripts for finish lab in Coursera course "Google IT Automation with Python". In general they perform following tasks:
- summarize and processe sales data into different categories 
- generate a PDF using Python
- automatically send a PDF by email
- check the health status of the system 

More detailed by scripts:

--- changeImage.py ---

- converts .tiff images to .jpeg format, while also:
- resizing them to 600x400 pixels
- removing alpha transparency (if the .tiff has it)
- saving the new images in the same directory

--- supplier_image_upload.py ---

- take the jpeg images from the supplier-data/images directory that we processed previously
- upload them to the web server fruit catalog.

--- run.py ---

- read fruit description data from .txt files
- convert that data into JSON {"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, ... blood pressure.", "image_name": "010.jpeg"}
- send it to a web server using a POST request.

--- reports.py ---

- generate a simple PDF report

--- emails.py ---

- create and send emails with optional attachments

--- report_email.py ---

- read descriptions	from .txt files
- create report content
- generate PDF report	using reports.generate()
- compose email	using emails.generate_email()
- send email using emails.send_email()

--- health_check.py ---

- run the monitoring checks and send email alerts if any check fails

| Check                    | Condition for Alert          | Email Subject                                       |
| ------------------------ | ---------------------------- | --------------------------------------------------- |
| CPU usage                | Above 80%                    | "Error - CPU usage is over 80%"                     |
| Disk space               | Less than 20% free           | "Error - Available disk space is less than 20%"     |
| Available memory         | Less than 100 MB             | "Error - Available memory is less than 100MB"       |
| localhost DNS resolution | Doesn't resolve to 127.0.0.1 | "Error - localhost cannot be resolved to 127.0.0.1" |

To test out script install the stress tool.
``` 
sudo apt install stress
```
Next, call the tool using a good number of CPUs to fully load our CPU resources:
```
stress --cpu 8 &
```
Hit Enter and allow the stress test to run in the background, as it will maximize our CPU utilization.

Now run health_check.py python script. 
Check appropriate inbox for any new email.
You should receive the email with the subject Error - CPU usage is over 80%.

To list all running jobs, use the following command:
```
jobs -l
```
Note down the process ID that is stress testing the CPU i.e., stress --cpu 8 &.
Then, terminate the stress testing process, using the following command.
```
kill [process-id]
```
Replace [process-id] with the process ID you noted down earlier.

For automation monitoring you can set a cron job that executes the script health_check.py every 60 seconds and sends health status via email according to script.

To set a user cron job use the following command:
```
crontab -e
```
in opened window you might write:

```
* * * * * /usr/bin/python3 /home/user/final_lab/health_check.py >> /home/user/cron.log 2>&1
```

The line ">> /home/user/cron.log 2>&1" means "logs all output (for example, print() command) and errors into /home/user/cron.log for later review".
