import sys
sys.path.append('./trainer')
import nutszebra_cifar10
import nutszebra_optimizer
import network_in_network
import argparse
import trainer.nutszebra_data_augmentation as da

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='cifar10')
    parser.add_argument('--load_model', '-m',
                        default=None,
                        help='trained model')
    parser.add_argument('--load_optimizer', '-o',
                        default=None,
                        help='optimizer for trained model')
    parser.add_argument('--load_log', '-l',
                        default=None,
                        help='optimizer for trained model')
    parser.add_argument('--save_path', '-p',
                        default='./',
                        help='model and optimizer will be saved at every epoch')
    parser.add_argument('--epoch', '-e', type=int,
                        default=int(1.2e5 / (50000. / 128)),
                        help='maximum epoch')
    parser.add_argument('--batch', '-b', type=int,
                        default=128,
                        help='mini batch number')
    parser.add_argument('--gpu', '-g', type=int,
                        default=-1,
                        help='-1 means cpu, put gpu id here')
    parser.add_argument('--start_epoch', '-s', type=int,
                        default=1,
                        help='start from this epoch')
    parser.add_argument('--train_batch_divide', '-trb', type=int,
                        default=1,
                        help='divid train batch number by this')
    parser.add_argument('--test_batch_divide', '-teb', type=int,
                        default=1,
                        help='divid test batch number by this')
    parser.add_argument('--lr', '-lr', type=float,
                        default=0.1,
                        help='leraning rate')

    args = parser.parse_args().__dict__
    lr = args.pop('lr')

    print('generating model')
    model = network_in_network.Network_In_Network(10)
    print('Done')
    optimizer = nutszebra_optimizer.OptimizerNetworkInNetwork(model, lr=lr)
    args['model'] = model
    args['optimizer'] = optimizer
    args['da'] = da.DataAugmentationCifar10NormalizeSmall
    main = nutszebra_cifar10.TrainCifar10(**args)
    main.run()
