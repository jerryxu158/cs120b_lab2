/*	Author: Jerry Xu
 *  Partner(s) Name: 
 *	Lab Section: 22
 *	Assignment: Lab 2 Exercise 4(challenge)
 *	Exercise Description: An amusement park kid ride cart has three seats, with 8-bit weight sensors 
 *	connected to ports A, B, and C (measuring from 0-255 kilograms). 
 *	Set PD0 to 1 if the cart's total passenger weight exceeds the maximum of 140 kg. 
 *	Also, the cart must be balanced: Set port PD1 to 1 f the difference between A and C exceeds 80 kg.  
 *	The remaining 6 bits on D should display an approximation of the total combined weight.
 *	Hint: You don’t have enough bits to represent the complete value; you only need to represent the most significant bits. 
 *	Interesting note: Disneyland recently redid their "It's a Small World" ride because the average passenger weight has increased over the years, causing more boats to get stuck on the bottom.
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif    

int main(void) {
    DDRA = 0x00; PORTA = 0xFF; // Configure port A's 8 pins as inputs
    DDRB = 0x00; PORTB = 0xFF; // Configure port B's 8 pins as outputs, initialize to 0s
    DDRC = 0x00; PORTC = 0xFF; // config portC's 8pins as outs, initialize to 0?
    DDRD = 0xFF; PORTD = 0x00;
    //unsigned char tmpB = 0x00; // Temporary variable to hold the value of B
    unsigned char tmpA = 0x00; // Temporary variable to hold the value of A
    unsigned char tmpB = 0x00;
    unsigned char tmpC = 0x00;
    unsigned char tmpD = 0x00;
    unsigned short overflow = 0;
    
    const unsigned char uc_maxWeight = 140;
	while(1) {
		tmpA = PINA;
		tmpB = PINB;
		tmpC = PINC;
		overflow = tmpA + tmpB + tmpC;

		tmpD = overflow >> 2;

		tmpD = tmpD & 0xFC;

		if((tmpA + tmpB + tmpC) > uc_maxWeight){
			tmpD = tmpD | 0x01;
		}
		if(((tmpA - tmpC) > 80) || ((tmpC - tmpA) > 80)){
			tmpD = tmpD | 0x02;
		}
		PORTD =tmpD;
	}
    return 0;
}
