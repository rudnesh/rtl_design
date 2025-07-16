module full_adder(
    input a,
    input b,
    input cin,
    output sum,
    output cout
);

assign sum = a ^ b ^ cin;
assign cout = (a & b) | (b & cin) | (cin & a);
initial begin
  $dumpfile("dump.vcd");       // Creates a VCD waveform file
  $dumpvars(0, full_adder);    // Dumps all signals in the full_adder module
end
endmodule

