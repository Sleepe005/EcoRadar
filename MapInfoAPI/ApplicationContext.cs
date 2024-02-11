using MapInfoAPI.Models;
using Microsoft.EntityFrameworkCore;

namespace MapInfoAPI
{
    public class ApplicationContext : DbContext
    {
        private DbSet<ExternalFactorsModel> externalFactors;

        public DbSet<ExternalFactorsModel> ExternalFactors { get => externalFactors; set => externalFactors = value; }

        public ApplicationContext(DbContextOptions option) : base(option) { }
    }
}
