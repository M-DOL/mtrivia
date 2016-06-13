/**
 * Created by Matt on 5/20/2016.
 **/
"use strict";

var num1 = document.getElementById('num1'), num2 = document.getElementById('num2'), res;
function add()
{
    if(num2.value !== "")
    {
        res = parseInt(num1.value) + parseInt(num2.value);
        output();
    }
}
function subtract()
{
    if(num2.value !== "")
    {
        res = parseInt(num1.value) - parseInt(num2.value);
        output();
    }
}
function mult()
{
    if(num2.value !== "")
    {
        res = parseInt(num1.value) * parseInt(num2.value);
        output();
    }
}
function divide()
{
    if(num2.value !== "")
    {
        res = parseInt(num1.value) / parseInt(num2.value);
        output()
    }
}
function output()
{
    num1.value = res;
    num2.value = "";
}