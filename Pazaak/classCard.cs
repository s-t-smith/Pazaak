using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pazaak
{
    internal class Card
    {
        // Fields:
        public int Val { get; protected set; }

        // Methods:
        protected Card() { }
        protected Card(int val) { }
        
    }
}
