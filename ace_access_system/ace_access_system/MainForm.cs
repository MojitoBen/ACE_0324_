using System.Data;
using MySql.Data.MySqlClient;

namespace ace_access_system

{
    public partial class MainForm : Form
    {
        private readonly System.Timers.Timer timer;
        public MainForm()
        {
            InitializeComponent();

            timer = new System.Timers.Timer(1000) { AutoReset = true };
            timer.Elapsed += Timer_Now_Tick;
            timer.Start();
        }

        private void button_contact_Click(object sender, EventArgs e)
        {
            Form_member mForm_member = new();
            mForm_member.Show();
        }

        private void �Τ��TToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form_member mForm_member = new();
            mForm_member.Show();
        }

        private void button_door_permission_Click(object sender, EventArgs e)
        {
            Form_Permission mForm_permission = new();
            mForm_permission.Show();
        }

        private void Timer_Now_Tick(object? sender, System.Timers.ElapsedEventArgs e)
        {
            this.InvokeAction(() =>
            {
                label_DateTime.Text = "�{�b�ɶ��G " + $"{DateTime.Now:yyyy/MM/dd}" + "     " + $"{DateTime.Now:HH:mm:ss}";
            });
        }

        private void label_DateTime_Click(object sender, EventArgs e)
        {

        }

        private void ���U�ק�b��ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form_Register mForm_Register = new();
            mForm_Register.Show();
        }
    }
}