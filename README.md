# 🔍 Automate Stop EC2 Instances
Automatically stop instances with Lambda, reduce your AWS usage fee!!

## Requirement
- AWS Account

## Installation
1. Create Python 3 Lambda Function
   paste lambda_function.py
   * you must change AWS_ACCESS_KEY and AWS_ACCESS_SECRET*
2. Set Cloudwatch Event for trigger
   if you want to Invoke every 22:00 UTC, set like this
   `cron(0 22 * * ? *)`

# 🤔 Anything Else
I wrote article about this function.
https://qiita.com/saitotak/536cb47f899f5ed86cce

# 🐑 Author
[saitotak](https://qiita.com/saitotak)

# ✍ License
[MIT](./LICENSE)

