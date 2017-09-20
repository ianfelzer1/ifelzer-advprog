
import java.io.*;
import java.util.*;

public class ArmstrongNumber
{ 
public static void main(String args[]) 
{

// Input number to check if its Armstrong number
System.out.println("Please enter a number to find if it is an Armstrong number: ");
int number = new Scanner(System.in).nextInt();

// Printing result
if(isArmStrong(number))
{
System.out.println(number + " is an Armstrong number");
}
else
{
System.out.println(number + " is not an Armstrong number");
}

} // End of main()

// Function returning true if number is Armstrong number or returning false

private static boolean isArmStrong(int number) 
{
int result = 0;
int dc=0; 
int orig = number;
while(orig != 0)
{ 
dc++; 
orig = orig/10;
}
orig = number;
while (orig!=0)
{
result = result + (int)Math.pow(orig%10, dc);
orig = orig/10;
}
if(number == result)
return true; 
else
return false;
} // End of isArmStrong() 
}

OUTPUT:
Please enter a number to find if it is an Armstrong number: 
9474
9474 is an Armstrong number

Please enter a number to find if it is an Armstrong number: 
8208
8208 is an Armstrong number


Ganesh RMarch 2, 2015 at 9:20 AM
package com.example.test.nover;
import java.util.List;
import java.util.ArrayList;
public class ArmstrongNumber {

public void findNumber() {
List numList = new ArrayList();
int newNum = 0;
String numVal= "";
int length = 0;
for(int i = 1000; i<=9999; i++) {
numVal = (numVal+i).trim();
length = numVal.length();
for(int j=0;j<length;j++) {
char charVal = numVal.charAt(j);
int charNum = charVal-'0';
charNum = (int) Math.pow(charNum,4);
//int charNo = (int) Math.pow(charNum,4);
newNum = newNum + charNum;
}
if(i==newNum) 
numList.add(i);
newNum = 0;
numVal="";
}
for(int i: numList) {
System.out.println("NUMBERS FOUND ARE " +i);
}
}

public static void main(String args[]) {
ArmstrongNumber numVer = new ArmstrongNumber();
numVer.findNumber();
}
}



Read more: http://www.java67.com/2012/07/java-program-to-find-armstrong-numbers.html#ixzz4NdLAPThY
