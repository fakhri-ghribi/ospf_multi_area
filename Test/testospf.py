from asyncio import tasks
from distutils import command
import imp
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import ipdb
nr= InitNornir(config_file="config.yml")

def pullospf(task):
    result = task.run(task=send_command, command="show ip ospf neighbor")
    task.host["facts"] = result.scrapli_response.genie_parse_output()

nr.run(task=pullospf)
ipdb.set_trace()