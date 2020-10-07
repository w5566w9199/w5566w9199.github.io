using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(MVC_SemanticAnalysisClient.Startup))]
namespace MVC_SemanticAnalysisClient
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
