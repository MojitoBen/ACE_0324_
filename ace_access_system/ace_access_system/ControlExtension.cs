using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ace_access_system
{
    public static class ControlExtension
    {
        public static void InvokeAction(this Control control, Action action, string TackTimeName = "")
        {
            try
            {
                if (control.InvokeRequired)
                {
                    control.Invoke(action);
                }
                else
                {
                    if (!string.IsNullOrWhiteSpace(TackTimeName))
                    {
                        Stopwatch sw = new();
                        sw.Start();
                        action();
                        sw.Stop();
                        
                    }
                    else
                    {
                        action();
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}
