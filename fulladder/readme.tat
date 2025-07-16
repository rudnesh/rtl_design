# STEP 1: Install required tools
sudo apt update
sudo apt install iverilog gtkwave python3-venv

# STEP 2: Create and activate Python virtual environment
python3 -m venv vlsienv
source vlsienv/bin/activate

# STEP 3: Install Cocotb inside the venv
pip install cocotb

# STEP 4: Write Verilog file as adder.v (containing waveform dump logic)

# STEP 5: Write Python testbench as tb.py

# STEP 6: Create Makefile with:
# - TOPLEVEL_LANG = verilog
# - VERILOG_SOURCES = $(PWD)/adder.v
# - TOPLEVEL = full_adder
# - MODULE = tb
# - SIM = icarus

# STEP 7: Run simulation
make

# STEP 8: View waveform in GTKWave
gtkwave dump.vcd

