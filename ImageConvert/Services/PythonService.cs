using System.Diagnostics;
using System.Text;

namespace ImageConvert.Services
{
    public class PythonService
    {
        public string Base(string path, string fileName, string scriptName, int range = 1, int threshold1 = 100, int threshold2 = 100)
        {
            Console.WriteLine($"Starting {scriptName} ...");

            var psi = new ProcessStartInfo();
            psi.FileName = @"C:\Users\elino\AppData\Local\Programs\Python\Python310\python.exe";
            var script = @"C:\OpenImageProcessor\PythonApplication1\" + scriptName + ".py";

            path = path.Replace("\r\n", String.Empty);
            psi.Arguments = script + " " + path + " " + fileName + " " + range + " " + threshold1 + " " + threshold2;

            psi.CreateNoWindow = true;
            psi.UseShellExecute = false;
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardError = true;

            var errors = "";
            var result = "";

            using (var process = Process.Start(psi))
            {
                errors = process?.StandardError.ReadToEnd();
                result = process?.StandardOutput.ReadToEnd();
            }

            Console.WriteLine("Errors");
            Console.WriteLine(errors);
            Console.WriteLine("result");
            Console.WriteLine(result);
            if(result != null)
            {
                return result;
            }
            else
            {
                return "undefined";
            }
        }
        public string CannyEdge(string path, string fileName)
        {
            return Base(path, fileName, "CannyEdge");
        }
        public string GetGray(string path, string fileName)
        {
            return Base(path, fileName, "PythonApplication1");
        }

        public string GenerateHistogram(string path, string fileName)
        {
            return Base(path, fileName, "histogram");
        }

        public string Equalize(string path, string fileName)
        {
            return Base(path, fileName, "Equalize");
        }

        public string Mediam(string path, string fileName, int range)
        {
            return Base(path, fileName, "Mediam", range);
        }

        public string Mediana(string path, string fileName, int range)
        {
            return Base(path, fileName, "Mediana", range);
        }

        public string Gaussian(string path, string fileName, int range)
        {
            return Base(path, fileName, "Gaussian", range);
        }

        public string Otsu(string path, string fileName, int range)
        {
            return Base(path, fileName, "Otsu", range);
        }

        public string Sobel(string path, string fileName, int range)
        {
            return Base(path, fileName, "Sobel", range);
        }

        public string AdaptativeSegmentation(string path, string fileName, int range)
        {
            return Base(path, fileName, "AdaptativeSegmentation", range);
        }

        public string ManualSegmentation(string path, string fileName, int range, int threshold1, int threshold2)
        {
            return Base(path, fileName, "ManualSegmentation", range, threshold1, threshold2);
        }

        public string Canny(string path, string fileName, int range, int threshold1, int threshold2)
        {
            return Base(path, fileName, "Canny", range, threshold1, threshold2);
        }

    }
}
