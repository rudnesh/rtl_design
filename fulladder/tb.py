# test_full_adder.py

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def full_adder_test(dut):
    """Test all input combinations for full adder"""

    for i in range(8):
        a = (i >> 2) & 1
        b = (i >> 1) & 1
        cin = i & 1

        dut.a.value = a
        dut.b.value = b
        dut.cin.value = cin

        await Timer(1, units='ns')  # Wait for 1 ns

        expected_sum = a ^ b ^ cin
        expected_cout = (a & b) | (b & cin) | (cin & a)

        assert dut.sum.value == expected_sum, f"SUM FAILED: {a}+{b}+{cin}"
        assert dut.cout.value == expected_cout, f"COUT FAILED: {a}+{b}+{cin}"

