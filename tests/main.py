import unittest
from core.common import OpsEnvironment
from examples.inventory import InventoryProviderEx
from ploy.core.resolvers import Registry


class TestMainMethod(unittest.TestCase):

    CTX = None
    PRODUCT = "ProductEx"
    ENV = "ProductEx:uat"

    def test_main(self):
        """
        target - lifecycle or phase

        """

        registry = Registry()
        registry.add_inventories(InventoryProviderEx(self.PRODUCT))
        env = registry.get_environment(self.ENV)

        for r in env:
            print(r)

        # ctx = Context(product=product)

        # task_name = args.get('<job>')
        # if args.get('--role') is not None:
        #     args['--role'] = args.get('--role').split(',')
        # if args.get('--module') is not None:
        #     args['--module'] = args.get('--module').split(',')
        # if args.get('--hosts') is not None:
        #     args['--hosts'] = set(args.get('--hosts').split(','))
        # # initialize Fabric settings
        # env.user = args['--login'] or ploy.ctx.product.environment.deployer.login
        # env.password = ploy.ctx.product.environment.deployer.password
        # if not env.password:
        #     env.key_filename = args['-i'] or ploy.ctx.product.environment.deployer.key
        # out = start(ploy.ctx, task_name, args.get('--role'), args.get('--modules'), args.get('--hosts'))
        # if len(out) > 0:
        #     print >> sys.stderr, '****************************************************'
        #     for rc in out:
        #         print >> sys.stderr, 'JOB: %s ERROR: %s' % (rc[0].name, rc[1])


