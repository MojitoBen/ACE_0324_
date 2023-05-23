using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.IO;
using System.Windows.Forms;
using System.Xml.Linq;

namespace ace_access_system
{
    public static class Static_Class
    {
        public static class TextBoxHelper
        {
            public static void Str_Keypress(object? sender, KeyPressEventArgs e)
            {
                if (!char.IsDigit(e.KeyChar) && e.KeyChar != (char)Keys.Back && e.KeyChar != (char)Keys.Delete)
                {
                    MessageBox.Show("請輸入數字！", "提示",
                        MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    e.Handled = true;
                }
            }//文字方塊只能輸數字

            public static void Passwd_Keypress(object? sender, KeyPressEventArgs e)
            {
                if (!char.IsLetter(e.KeyChar) && !char.IsDigit(e.KeyChar) && !char.IsControl(e.KeyChar) && e.KeyChar != (char)Keys.Back && e.KeyChar != (char)Keys.Delete)
                {
                    MessageBox.Show("請輸入英數字！", "提示",
                        MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    e.Handled = true;
                }
            }//文字方塊只能輸英數字
        }

        public static class Way
        {
            public static string GetWayName(int wayCode)
            {
                switch (wayCode)
                {
                    case 0:
                        return "關閉";
                    case 1:
                        return "雙向";
                    case 2:
                        return "只進";
                    case 3:
                        return "只出";
                    default:
                        return "未知";
                }
            }

            public static string ToString(int wayCode)
            {
                return GetWayName(wayCode);
            }

            public static int GetWayCode(string wayName)
            {
                switch (wayName)
                {
                    case "關閉":
                        return 0;
                    case "雙向":
                        return 1;
                    case "只進":
                        return 2;
                    case "只出":
                        return 3;
                    default:
                        return -1; // 或者返回一個特定的錯誤碼表示未知進出方向
                }
            }
        } //進出方向
        public static class EnableStatus
        {
            public static string GetEnableStatus(int enableCode)
            {
                switch (enableCode)
                {
                    case 0:
                        return "關閉中";
                    case 1:
                        return "使用中";
                    default:
                        return "未知";
                }
            }

            public static string ToString(int enableCode)
            {
                return GetEnableStatus(enableCode);
            }
        } //使用狀態

        public static class LogRecord
        { 

            public static void WriteLog(string message, string fileName)
            {
                string DIRNAME = Application.StartupPath + @"\Log\";
                string FILENAME = DIRNAME + fileName + DateTime.Now.ToString("yyyyMMdd") + ".txt";

                if (!Directory.Exists(DIRNAME))
                    Directory.CreateDirectory(DIRNAME);

                if (!File.Exists(FILENAME))
                {
                    File.Create(FILENAME).Close();
                }
                using (StreamWriter sw = File.AppendText(FILENAME))
                {
                    Log(message, sw);
                }
            }
            public static void ReadLog(string Date_yyyyMMdd)
            {
                string DIRNAME = AppDomain.CurrentDomain.BaseDirectory + @"\Log\";
                string FILENAME = DIRNAME + Date_yyyyMMdd + ".txt";

                if (File.Exists(FILENAME))
                {
                    using (StreamReader r = File.OpenText(FILENAME))
                    {
                        DumpLog(r);
                    }
                }
                else
                {
                    Console.WriteLine(Date_yyyyMMdd + ": No Data!");
                }
            }

            private static void DumpLog(StreamReader r)
            {
                string line;
                while ((line = r.ReadLine()) != null)
                {
                    Console.WriteLine(line);
                }
            }
            private static void Log(string logMessage, TextWriter w)
            {
                w.Write("\r\nLog Entry : ");
                w.WriteLine("{0} {1}", DateTime.Now.ToLongTimeString(), DateTime.Now.ToLongDateString());
                w.WriteLine("  :");
                w.WriteLine("  :{0}", logMessage);
                w.WriteLine("-------------------------------");
            }
        }
    }
}
