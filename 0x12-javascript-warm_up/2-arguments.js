#!/usr/bin/node

const num = process.argv.length - 2;

if (num <= 0)
{
	console.log("No argument");
}
else
{
	console.log("Argument found");
}
