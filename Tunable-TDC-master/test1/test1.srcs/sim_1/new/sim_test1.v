`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/07/03 14:52:50
// Design Name: 
// Module Name: sim_test1
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


module sim_test1(

    );

    
        reg clk;
        wire [15:0] temp_out;
        wire [15:0] vccint_out;
    
        // 实例化待测试模块
        test1 uut (
            .clk(clk),
            .temp_out(temp_out),
            .vccint_out(vccint_out)
        );
    
        // 时钟生成
        initial begin
            clk = 0;
            forever #5 clk = ~clk;
        end
    
        // 仿真过程
        initial begin
            // 初始化
            $monitor("Time = %0d, Temp = %h, Vccint = %h", $time, temp_out, vccint_out);
            
            // 运行一段时间
            #1000;
            
            // 结束仿真
            $finish;
        end
    
    endmodule
