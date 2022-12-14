import nmap3
from scapy.all import *

from .models import (
    Host,
    OperativeSystemMatch,
    OperativeSystemClass,
    Port,
    PortService,
    ScannerHistory
)

class NmapScanner(object):

    def perform_full_scan_and_save(self, target, args="-A"):

        nmap = nmap3.Nmap()
        scanner_result = nmap.nmap_version_detection(target, args=args)

        scanner_history = ScannerHistory(
            target=target,
            type='FS'
        )

        scanner_history.save()

       

        IPList = list(scanner_result)

        for IP in IPList:

            host_data = {
                'IP': IP
            }

          

            if "macaddress" in scanner_result[IP]:

                if scanner_result[IP]["macaddress"] is not None:

                    if "addr" in scanner_result[IP]["macaddress"]:
                        host_data['mac_address'] = scanner_result[IP]["macaddress"]["addr"]

            host, created = Host.objects.get_or_create(**host_data)

            # Add host to scanner history (many to many relation)
            scanner_history.hosts.add(host)

            if "osmatch" in scanner_result[IP]:
                for osmatch in scanner_result[IP]["osmatch"]:

                    operative_system_match, created = OperativeSystemMatch.objects.get_or_create(
                        name=osmatch["name"],
                        accuracy=osmatch["accuracy"],
                        line=osmatch["line"],
                        host=host
                    )

                    if "osclass" in osmatch:

                        operative_system_class_data = {}

                        operative_system_class_data['operative_system_match'] = operative_system_match

                        if "type" in osmatch["osclass"]:
                            operative_system_class_data['type'] = osmatch["osclass"]["type"]

                        if "vendor" in osmatch["osclass"]:
                            operative_system_class_data['vendor'] = osmatch["osclass"]["vendor"]

                        if "osfamily" in osmatch["osclass"]:
                            operative_system_class_data['operative_system_family'] = osmatch["osclass"]["osfamily"]

                        if "osgen" in osmatch["osclass"]:
                            operative_system_class_data['operative_system_generation'] = osmatch["osclass"]["osgen"]

                        if "accuracy" in osmatch["osclass"]:
                            operative_system_class_data['accuracy'] = osmatch["osclass"]["accuracy"]

                        operative_system_class, created = OperativeSystemClass.objects.get_or_create(
                            **operative_system_class_data
                        )

            if "ports" in scanner_result[IP]:
                for ports in scanner_result[IP]["ports"]:

                    port = Port(
                        protocol=ports["protocol"],
                        portid=ports["portid"],
                        state=ports["state"],
                        reason=ports["reason"],
                        reason_ttl=ports["reason_ttl"],
                        host=host
                    )

                    port.save()

                    if "service" in ports:
                        port_service_data = {}

                        port_service_data['port'] = port

                        if "name" in ports["service"]:
                            port_service_data['name'] = ports["service"]["name"]

                        if "product" in ports["service"]:
                            port_service_data['product'] = ports["service"]["product"]

                        if "extrainfo" in ports["service"]:
                            port_service_data['extra_info'] = ports["service"]["extrainfo"]

                        if "hostname" in ports["service"]:
                            port_service_data['hostname'] = ports["service"]["hostname"]

                        if "ostype" in ports["service"]:
                            port_service_data['operative_system_type'] = ports["service"]["ostype"]

                        if "method" in ports["service"]:
                            port_service_data['method'] = ports["service"]["method"]

                        if "conf" in ports["service"]:
                            port_service_data['conf'] = ports["service"]["conf"]

                        port_service = PortService(
                            **port_service_data
                        )

                        port_service.save()

        return scanner_history


class ScapyScanner(object):

    def __init__(self):
        self.target = None

   
    def save_quick_scan(self):
        
        answered, unanswered = scapy.arping(self.target)

        scanner_history = ScannerHistory(
            target=self.target
        )

        scanner_history.save()

        for row in answered:

            original_packet, answer = row

            IP = answer.psrc
            mac_address = answer.hwsrc

            host, created = Host.objects.get_or_create(
                IP=IP,
                mac_address=mac_address
            )

            
            scanner_history.hosts.add(host)

        return scanner_history
