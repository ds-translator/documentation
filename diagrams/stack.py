from diagrams import Diagram, Edge
from diagrams.onprem.container import Docker
from diagrams.onprem.iac import Terraform
from diagrams.onprem.vcs import Github, Git
from diagrams.custom import Custom
from diagrams.programming.language import Python, Javascript

graph_attr = {
     "pad":"0"
 }


with Diagram("", filename="./images/stack", outformat="png", show=False, graph_attr=graph_attr):
    
        github = Github("")
        git = Git("")
        terraform = Terraform("")
        aws = Custom("", "../images/aws.png")
        docker = Docker("")
        python = Python("")
        javascript = Javascript("")
        kubernetes = Custom("", "../images/kubernetes.png")

        github >> Edge(style='invis') \
        >> git >> Edge(style='invis') \
        >> terraform >> Edge(style='invis') \
        >> aws >> Edge(style='invis') \

        docker >> Edge(style='invis') \
        >> python >> Edge(style='invis') \
        >> javascript >> Edge(style='invis') \
        >> kubernetes >> Edge(style='invis') \

