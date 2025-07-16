###############################################################
🎯 Verilog Design + Simulation + Schematic Visualization
Using: Yosys + NetlistSVG + GTKWave
###############################################################

This guide walks you through simulating a Verilog design, 
viewing waveform outputs, and generating a schematic 
from gate-level netlist — using ONLY open-source tools.

✅ Tools Required:
-------------------
1. Yosys       – for synthesis and netlist generation
2. GTKWave     – to view signal waveforms (dump.vcd)
3. NetlistSVG  – to create gate-level schematic from netlist
4. Icarus Verilog or Cocotb – for simulation (optional but helpful)
5. Node.js and npm – required by NetlistSVG

---------------------------------------------------------------
📦 STEP 1: Install Required Tools
---------------------------------------------------------------

# For Ubuntu/Debian-based systems:
sudo apt update
sudo apt install yosys gtkwave iverilog python3 python3-pip -y
sudo apt install nodejs npm -y

# Install netlistsvg (via npm)
sudo npm install -g netlistsvg

# (Optional) Create Python virtual environment if using Cocotb
python3 -m venv vlsienv
source vlsienv/bin/activate
pip install cocotb

---------------------------------------------------------------
🧾 STEP 2: Write your Verilog Design (Example: full_adder.v)
---------------------------------------------------------------

module full_adder(input a, b, cin, output sum, cout);
    assign sum = a ^ b ^ cin;
    assign cout = (a & b) | (b & cin) | (a & cin);
endmodule

---------------------------------------------------------------
💥 STEP 3: Simulate to Generate Waveform (dump.vcd)
---------------------------------------------------------------

# Add this inside your Verilog testbench or module
initial begin
    $dumpfile("dump.vcd");
    $dumpvars(0, full_adder);
end

# Compile and run with Icarus Verilog
iverilog -o sim.out full_adder.v tb.v
./sim.out

# OR use Cocotb (if set up)
make MODULE=tb TOPLEVEL=full_adder

---------------------------------------------------------------
👀 STEP 4: View Waveform Using GTKWave
---------------------------------------------------------------

gtkwave dump.vcd

You will see signal transitions for all your testbench inputs/outputs.

---------------------------------------------------------------
🧠 STEP 5: Generate Netlist using Yosys
---------------------------------------------------------------

yosys -p "read_verilog full_adder.v; prep -top full_adder; write_json full_adder.json"

This will produce: full_adder.json

---------------------------------------------------------------
🖼 STEP 6: Generate Schematic with NetlistSVG
---------------------------------------------------------------

netlistsvg full_adder.json -o full_adder.svg

# To open and view
xdg-open full_adder.svg

You will see a clean, labeled RTL/gate-level schematic!

---------------------------------------------------------------
🎉 DONE!
---------------------------------------------------------------

You now have:
- Waveform in GTKWave ✅
- Clean schematic in SVG ✅
- Full open-source flow ✅

📁 Output Files:
---------------
- `dump.vcd`         → waveform
- `full_adder.json`  → netlist
- `full_adder.svg`   → schematic image

Happy hacking!
Open-source VLSI FTW 💻⚡🧠

