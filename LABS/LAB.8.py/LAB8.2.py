# Define a simple User class
class User:
    def __init__(self, name, role="user"):
        self.name = name
        self.role = role

    def check_privilege(self):
        return self.role

    def __eq__(self, other):
        return isinstance(other, User) and self.name == other.name

    def __repr__(self):
        return f"User({self.name}, role={self.role})"

# Your Device class
class Device:

    def __init__(self, device_id, device_type, owner):
        self.device_id = device_id
        self.device_type = device_type
        self.owner = owner
        self.compliance = True
        self.active = True

    def authorise_access(self, user):
        if not self.compliance:
            print("Device not compliant")
            return False

        if user.check_privilege() == "admin":
            print("Admin access granted")
            return True

        if user == self.owner:
            print("Owner access granted")
            return True

        print("Access denied")
        return False

    def quarantine(self, user):
        if user.check_privilege() == "admin":
            self.active = False
            print("Device quarantined")
        else:
            print("Only admin can quarantine")

# --- Example usage ---

# Create some users
alice = User("Alice")          # Normal user
bob = User("Bob")              # Normal user
admin = User("Carol", role="admin")  # Admin user

# Create a device owned by Alice
device1 = Device(device_id=101, device_type="Laptop", owner=alice)

# Try accessing the device
print("\n--- Access Tests ---")
device1.authorise_access(alice)   # Owner access
device1.authorise_access(bob)     # Denied
device1.authorise_access(admin)   # Admin access

# Try quarantining the device
print("\n--- Quarantine Tests ---")
device1.quarantine(bob)    # Should fail
device1.quarantine(admin)  # Should succeed

# Check device status
print("\nDevice Active Status:", device1.active)