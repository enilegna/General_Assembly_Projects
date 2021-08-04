# Resnet18 Model - Run 4

 - Resnet18 pretrained model was loaded 
 - Layers in model were frozen to keep weights intact, preventing backward weight propogation
- Initial Learning Rate of 0.001
- Learning Rate Scheduler was used at a factor of 0.1 with patience 3

## Codes Used
### Freezing layers in pretrained model
**Loading Pretrained Resnet18 Model**

    #load resnet18 pretrained model
    resnet18 = torchvision.models.resnet18(pretrained=True)
    
    #freeze weights in pretrained model (remove if we want to hypertune and update the weights)
    for param in resnet18.parameters():
	    param.requires_grad = False
	
	#show layers
	print(resnet18)
    


### Using Learning Rate Scheduler
**Modify Layers**

    lr = 0.001
    
    # Parameters of newly constructed modules have requires_grad=True by default
    #change output features from pretrain 1000 to 3 as we only have 3 classes
    
    resnet18.fc = torch.nn.Linear(in_features=512, out_features=3)
    
    #Declare criterion
    loss_fn = torch.nn.CrossEntropyLoss()
    
    #Declare adam optimizer with a learning rate 
    optimizer = torch.optim.Adam(resnet18.parameters(), lr=lr)
    
    '''
    STEP 7: INSTANTIATE STEP LEARNING SCHEDULER CLASS
    '''
    
    # lr = lr * factor
    # mode='max': look for the maximum validation accuracy to track
    # patience: number of epochs - 1 where loss plateaus before decreasing LR
    # patience = 0, after 1 bad epoch, reduce LR
    # factor = decaying factor
    
    scheduler = ReduceLROnPlateau(optimizer, 'min', factor=0.1, patience=3, verbose=True)

**The Training Function**

    def test(dataloader, model, loss_fn):
        image_id, predictions, targets, probabilities= [], [], [], []
        size = len(dataloader.dataset)
        num_batches = len(dataloader)
        model.eval()
        test_loss, test_acc = 0, 0
        with torch.no_grad():
            for _, (name, image, labels) in enumerate(dataloader):
                # Compute prediction error
                output = model(image)
                test_loss += loss_fn(output, labels).item()
                # get predictions for train data
                yhat = output.argmax(1)
                test_acc += (yhat == labels).type(torch.float).sum().item()
                for i in range(len(name)):
                    image_id.append(name[i])
                    predictions.append(int(yhat[i]))
                    targets.append(int(labels[i]))
                    probabilities.append(output[i])
        pred_df = pd.DataFrame({'image': image_id, 'targets': targets, 'predictions': predictions, 'probabilities': probabilities})
        curr_lr = optimizer.param_groups[0]['lr']
        
    
        test_loss /= num_batches
        test_acc /= size
        
        show_preds()
        print(f"Test Error: \n Accuracy: {(100*test_acc):>0.1f}%, Avg loss: {test_loss:>8f}, LR:{curr_lr} \n")
        return test_acc, test_loss, pred_df

**The Training Loop**

    epochs = 6
    count = 0
    start = time.time()
    
    # lists to store per-epoch loss and accuracy values
    history = {} 
    history['loss'] = []
    history['val_loss'] = []
    history['acc'] = []
    history['val_acc'] = []
    
    for e in range(epochs):
    
        print(f"Epoch {e+1}\n-------------------------------")
        
        #train model and get accuracy and loss values
        train_acc, train_loss = train(dl_train, resnet18, loss_fn, optimizer)
        #evaluate model and get accuracy, loss and predictions
        test_acc, test_loss, predictions = test(dl_test, resnet18, loss_fn)
        scheduler.step(test_loss)
        
        # store per-epoch loss and accuracy values
        history['loss'].append(train_loss)
        history['val_loss'].append(test_loss)
        history['acc'].append(train_acc)
        history['val_acc'].append(test_acc)
    
        if test_acc >= 0.97 :
          count += 1
          print('Performance condition satisfied, saving model..')
          #save model as .pth file
          torch.save(resnet18.state_dict(), os.path.join('/content/drive/MyDrive/Capstone/Models/Resnet18-4/',f'resnet18_epoch{e+1}.pth'))
          #save model predictions as .csv file
          predictions.to_csv(predictions, os.path.join('/content/drive/MyDrive/Capstone/Models/Resnet18-4/',f'resnet18_epoch{e+1}.csv'))
    
    print(f'Done! {count} models saved in Capstone Models folder')
    
    #save accuracy and loss history into csv
    Resnet18History = pd.DataFrame(history)
    Resnet18History.to_csv('/content/drive/MyDrive/Capstone/Models/Resnet18-4/resnethistory.csv', index=False)
    
    print(f'/n Loss history saved in Capstone Models folder')
    end = time.time()
    print(f"Training time: {(end-start)/60:.3f} minutes")

