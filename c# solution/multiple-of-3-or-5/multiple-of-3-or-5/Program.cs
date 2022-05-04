using System;

namespace multiple_of_3_or_5
{
    class Program
    {
        static void Main(string[] args)
        {
            int total = 0;

            for (int i = 1; i < 1000; i++)
            {
                if ((i % 3 == 0) || (i % 5 == 0))
                {
                    total += i;
                }
            }

            Console.Write(total);
            Console.Read();
        }
    }
}
