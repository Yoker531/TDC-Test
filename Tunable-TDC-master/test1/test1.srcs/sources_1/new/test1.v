`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/07/03 14:48:37
// Design Name: 
// Module Name: test1
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module test1(
input wire clk,
    output wire [15:0] temp_out,
    output wire [15:0] vccint_out
);

    // XADCԭ��ģ��ʵ����
    wire [15:0] do_out;
    wire [6:0] daddr_in = 7'h00;  // ��ַ����
    wire den_in = 1'b1;           // ʹ������
    wire dwe_in = 1'b0;           // дʹ������
    wire [15:0] di_in = 16'h0000; // ��������
    wire drdy_out;                // ����׼�����
    wire eoc_out;                 // ת��������
    wire channel_out;             // ͨ�����
    wire [15:0] vauxp = 16'h0000; // ������������
    wire [15:0] vauxn = 16'h0000; // �������븺��

    // XADCԭ��ʵ��
    XADC #(
        .INIT_40(16'h3000), // ����XADCͨ������
        .INIT_41(16'h2FFF), 
        .INIT_42(16'h0400), 
        .INIT_44(16'h0800), 
        .INIT_45(16'h0000), 
        .INIT_46(16'h0000), 
        .INIT_47(16'h0000), 
        .INIT_48(16'h0700), 
        .INIT_49(16'h0000), 
        .INIT_4A(16'h0000), 
        .INIT_4B(16'h0000), 
        .INIT_4C(16'h0000), 
        .INIT_4D(16'h0000), 
        .INIT_4E(16'h0000), 
        .INIT_4F(16'h0000), 
        .IS_DCLK_INVERTED(1'b0)
    ) XADC_inst (
        .DO(do_out),
        .DRDY(drdy_out),
        .DADDR(daddr_in),
        .DCLK(clk),
        .DEN(den_in),
        .DI(di_in),
        .DWE(dwe_in),
        .VAUXP(vauxp),
        .VAUXN(vauxn),
        .VP(),
        .VN(),
        .EOS(eoc_out),
        .CHANNEL(channel_out)
    );

    // �򵥵�״̬������ȡ�¶Ⱥ͵�ѹ��Ϣ
    reg [15:0] temp_reg;
    reg [15:0] vccint_reg;

    always @(posedge clk) begin
        if (drdy_out) begin
            case (channel_out)
                7'h00: temp_reg <= do_out;   // �¶ȴ�����
                7'h11: vccint_reg <= do_out; // Vccint��ѹ
            endcase
        end
    end

    assign temp_out = temp_reg;
    assign vccint_out = vccint_reg;

endmodule
