from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.aws.storage import SimpleStorageServiceS3 as S3
from diagrams.oci.network import LoadBalancer
from diagrams.oci.compute import OKE, Container

graph_attr = {
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "1.0",  # Adjust node separation
    "ranksep": "1.2",  # Adjust rank separation between nodes
    "fontsize": "12",
    "fontname": "Helvetica",
    "bgcolor": "white"
}

class Services:
    def __init__(self):
        self.translate = Container("Translate")
        self.backend = Container("Backend Server")
        self.webserver = Container("Web Server")    
        self.stt = Container("STT")
        self.tts = Container("TTS")

with Diagram("", filename="./images/simplified", direction="TB", outformat="png", show=False, graph_attr=graph_attr):

        users = Users("End Users")
        lb = LoadBalancer("Load Balancer")
        ce = OKE("Kubernetes Cluster")
        services = Services()
        
        users - lb - ce

        ce - Edge(label="") - services.translate
        ce - Edge(label="") - services.backend
        ce - Edge(label="") - services.webserver       
        ce - Edge(label="") - services.stt
        ce - Edge(label="") - services.tts