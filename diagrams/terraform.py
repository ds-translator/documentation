from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.aws.storage import SimpleStorageServiceS3 as S3
from diagrams.oci.network import LoadBalancer
from diagrams.oci.compute import OKE, Container
from diagrams.onprem.iac import Terraform
from diagrams.oci.security import IDAccess
from diagrams.oci.compute import VM
from diagrams.oci.storage import FileStorage
from diagrams.oci.database import DatabaseService as Infrastructure

graph_attr = {
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "1.0",  # Adjust node separation
    "ranksep": "1.2",  # Adjust rank separation between nodes
    "fontsize": "12",
    "fontname": "Helvetica",
    "bgcolor": "white"
}

class Team:
    def __init__(self):
        self.janod = User("Janods IAM account")
        self.julian = User("Julians IAM account")
        self.patrick = User("Patricks IAM account")  

with Diagram("", filename="./images/terraform", direction="TB", outformat="png", show=False, graph_attr=graph_attr):

        team = Team()

        terraform = Terraform("")
        
        
        # ec2 = VM()
        
        iam = IDAccess("IAM role")

        with Cluster("AWS"):
            infrastructure = Infrastructure("Infrastructure")
            s3 = FileStorage("Terraform state\nfile (S3)")
            
    
        [team.janod, team.julian, team.patrick] >> iam
        
        iam >> terraform << Edge() >> s3

        terraform >> infrastructure