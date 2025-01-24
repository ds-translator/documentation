from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EKS, ECS
from diagrams.aws.network import ELB, VPC
from diagrams.aws.devtools import Codecommit
from diagrams.onprem.container import Docker
from diagrams.generic.blank import Blank
from diagrams.onprem.client import Client, User, Users
from diagrams.onprem.ci import GithubActions
from diagrams.aws.security import IdentityAndAccessManagementIamAddOn
from diagrams.oci.security import IDAccess
from diagrams.onprem.iac import Terraform
from diagrams.oci.compute import BM
from diagrams.oci.devops import APIService
from diagrams.aws.storage import SimpleStorageServiceS3 as S3
from diagrams.aws.management import AmazonManagedPrometheus as Prometheus, AmazonManagedGrafana as Grafana
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

