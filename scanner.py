#!/usr/bin/python3

import nmap
import argparse
from datetime import datetime

def run_scan(target, ports, scan_type, output_file):
    scanner = nmap.PortScanner()

    scan_options = {
        "syn": ("-sS", "tcp"),
        "udp": ("-sU", "udp"),
        "full": ("-sS -sV -sC -A -O", "tcp")
    }

    if scan_type not in scan_options:
        print("Invalid scan type")
        return

    scan_flag, protocol = scan_options[scan_type]

    print("\nStarting scan...\n")

    try:
        scanner.scan(target, ports, scan_flag + " -Pn")

        print("Nmap version:", scanner.nmap_version())

        if target not in scanner.all_hosts():
            print("Host is down or not reachable")
            return

        print("\nHost:", target, "is up\n")

        result_lines = []

        for proto in scanner[target].all_protocols():
            print("Protocol:", proto)

            ports_list = scanner[target][proto].keys()

            for port in sorted(ports_list):
                state = scanner[target][proto][port]["state"]
                service = scanner[target][proto][port].get("name", "unknown")

                line = f"Port {port}: {state} ({service})"
                print(line)
                result_lines.append(line + "\n")

        if output_file:
            with open(output_file, "w") as f:
                f.writelines(result_lines)
            print("\nResults saved to", output_file)

    except Exception as e:
        print("Error:", e)


def main():
    parser = argparse.ArgumentParser(description="Simple Python Nmap Scanner")

    parser.add_argument("-t", "--target", required=True, help="Target IP")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range")
    parser.add_argument("-s", "--scan", default="syn", help="Scan type (syn/udp/full)")
    parser.add_argument("-o", "--output", help="Save output to file")

    args = parser.parse_args()

    print("===================================")
    print(" Python Nmap Scanner")
    print("===================================")
    print("Target:", args.target)
    print("Ports:", args.ports)
    print("Scan type:", args.scan)
    print("===================================")

    start = datetime.now()

    run_scan(args.target, args.ports, args.scan, args.output)

    end = datetime.now()
    print("\nTime taken:", end - start)


if __name__ == "__main__":
    main()