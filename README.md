# **To Build container:**

docker build -t router_app:latest .

# **To run container:**

docker run -itd -p 5000:5000 router_app:latest

# **Test with python client:**

python client_for_testing.py
