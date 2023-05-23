using System.Globalization;

namespace ace_access_system
{
    internal static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            //InputLanguage.DefaultInputLanguage = InputLanguage.FromCulture(englishCulture);
            // To customize application configuration such as set high DPI settings or default font,
            // see https://aka.ms/applicationconfiguration.
            ApplicationConfiguration.Initialize();
            //Application.Run(new MainForm());
            Application.Run(new Form_Login()); //啟動時需要帳號密碼
        }
    }
}