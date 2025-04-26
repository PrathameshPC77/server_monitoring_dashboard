# monitor/management/commands/generate_mock_data.py
from django.core.management.base import BaseCommand
from monitor.models import Server, ServerMetrics
import random
from django.utils import timezone

class Command(BaseCommand):
    help = 'Generates mock server and metrics data for testing'

    def add_arguments(self, parser):
        parser.add_argument(
            '--servers',
            type=int,
            default=3,
            help='Number of servers to create (default: 3)'
        )
        parser.add_argument(
            '--metrics',
            type=int,
            default=50,
            help='Metrics per server to create (default: 50)'
        )

    def handle(self, *args, **options):
        server_count = options['servers']
        metrics_count = options['metrics']
        
        self.stdout.write(self.style.SUCCESS(f'Creating {server_count} servers with {metrics_count} metrics each...'))
        
        #delete the existing data
        ServerMetrics.objects.all().delete()
        Server.objects.all().delete()
        
        # creating servers
        servers = []
        for i in range(1, server_count + 1):
            server = Server.objects.create(
                name=f"{random.choice(['Web', 'DB', 'App', 'API', 'Cache'])} Server {i}",
                ip_address=f"192.168.1.{i}",
                location=random.choice(['Data Center A', 'Data Center B', 'Cloud East']),
                status=random.choice([True, True, True, False])  # 75% chance of being online
            )
            servers.append(server)
            self.stdout.write(f'Created server: {server.name} ({server.ip_address})')

        base_time = timezone.now().replace(minute=0, second=0, microsecond=0)
        #Create metrics for each server
        for i, server in enumerate(servers):
            for j in range(metrics_count):
                ServerMetrics.objects.create(
                    server=server,
                    cpu_usage=random.uniform(0, 100),
                    memory_usage=random.uniform(0, 100),
                    disk_usage=random.uniform(0, 100),
                    network_in=random.uniform(0, 100),
                    network_out=random.uniform(0, 50),
                    alert_level=self._get_alert_level(),
                    timestamp=base_time - timezone.timedelta(
                        hours=i,  
                        minutes=j*15  
                    )
                )
            self.stdout.write(f'Created {metrics_count} metrics for {server.name}')

        self.stdout.write(self.style.SUCCESS('Successfully generated mock data!'))

    def _get_alert_level(self):
        # 10% critical, 20% medium, 30% low, 40% no alert
        rand = random.random()
        if rand < 0.1:
            return 'critical' # 10% critical
        elif rand < 0.3:
            return 'medium' #20% medium
        elif rand < 0.6:
            return 'low' #30% low
        else:
            return 'low' # 40% no alert