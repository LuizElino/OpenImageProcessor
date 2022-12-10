// See https://aka.ms/new-console-template for more information
using IronPython.Hosting;
using System.Diagnostics;
using System.Text;

Console.WriteLine("Python Whithout any lib");

var psi = new ProcessStartInfo();
psi.FileName = @"C:\Users\elino\AppData\Local\Programs\Python\Python310\python.exe";
var script = @"C:\Users\elino\source\repos\PythonApplication1\PythonApplication1\PythonApplication1.py";
var file = @"C:/Users/elino/source/repos/PythonApplication1/ConsoleApp1/Imgs/Inputs/subsolo.jpg";
psi.Arguments = script + " " + file;

psi.CreateNoWindow = true;
psi.UseShellExecute = false;
psi.RedirectStandardOutput = true;
psi.RedirectStandardError = true;

var results = "";
var errors = "";

using (var process = Process.Start(psi))
{
    results = process.StandardOutput.ReadToEnd();
    errors = process.StandardError.ReadToEnd();
}

Console.WriteLine("Errors:");
Console.WriteLine(errors);
Console.WriteLine("Results:");
Console.WriteLine(results);

//Console.WriteLine("Iron Python");

//var engine = Python.CreateEngine();

//var script = "C:\\Users\\elino\\source\\repos\\PythonApplication1\\PythonApplication1\\PythonApplication1.py";
//var source = engine.CreateScriptSourceFromFile(script);

//var argv = new List<string>();
//argv.Add("");
//argv.Add("Elino");
//argv.Add("João");

//engine.GetSysModule().SetVariable("argv", argv);

//var eIO = engine.Runtime.IO;
//var errors = new MemoryStream();
//eIO.SetErrorOutput(errors, Encoding.Default);
//var results = new MemoryStream();
//eIO.SetOutput(results, Encoding.Default);

//var scope = engine.CreateScope();
//source.Execute(scope);

//string str(byte[] data) => Encoding.Default.GetString(data);

//Console.WriteLine("Errors:");
//Console.WriteLine(str(errors.ToArray()));
//Console.WriteLine("Results:");
//Console.WriteLine(str(results.ToArray()));