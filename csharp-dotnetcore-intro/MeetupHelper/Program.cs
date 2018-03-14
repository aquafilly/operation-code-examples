using System;

namespace MeetupHelper
{
    class Program
    {
        static void Main(string[] args)
        {
            var meetup = new Meetup();

            meetup.Name = "Operation Code";

            meetup.Organizers.Add("James (O)");
            meetup.Organizers.Add("Shirley (O)");

            meetup.Attendees.Add("Mary (A)");
            meetup.Attendees.Add("Ben (A)");
            meetup.Attendees.Add("Jack (A)");
            meetup.Attendees.Add("Debra (A)");
            meetup.Attendees.Add("Antonio (A)");
            meetup.Attendees.Add("Evette (A)");
            meetup.Attendees.Add("William (A)");
            meetup.Attendees.Add("Cheryl (A)");
            meetup.Attendees.Add("Levi (A)");

            meetup.Start();
            Console.WriteLine(Environment.NewLine);
            Console.WriteLine("Meetup in progress. Fun stuff is happening and people are learning. Press enter to continue...");
            Console.ReadLine();

            meetup.End();
            Console.WriteLine(Environment.NewLine);
            Console.WriteLine("Meetup has ended. Let's go home. Press enter to continue...");
            Console.ReadLine();
        }
    }
}
