import datetime

class SecurityAudits:
    def __init__(self):
        self.audit_logs = []

    def schedule_audit(self, audit_name, date_time):
        # Schedule a new security audit
        audit = {
            'name': audit_name,
            'scheduled_time': date_time,
            'status': 'Scheduled'
        }
        self.audit_logs.append(audit)
        return f"Audit '{audit_name}' scheduled for {date_time}"

    def conduct_audit(self, audit_name):
        # Conduct the scheduled audit
        for audit in self.audit_logs:
            if audit['name'] == audit_name and audit['status'] == 'Scheduled':
                audit['status'] = 'Completed'
                audit['completion_time'] = datetime.datetime.now()
                return f"Audit '{audit_name}' completed successfully"
        return f"Audit '{audit_name}' not found or already completed"

    def generate_compliance_report(self):
        # Generate a compliance report based on completed audits
        report = "Compliance Report\n"
        report += "================\n"
        for audit in self.audit_logs:
            if audit['status'] == 'Completed':
                report += f"Audit Name: {audit['name']}\n"
                report += f"Scheduled Time: {audit['scheduled_time']}\n"
                report += f"Completion Time: {audit['completion_time']}\n"
                report += "----------------\n"
        return report
