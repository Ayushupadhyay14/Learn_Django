from django.shortcuts import render
import qrcode
from .models import QRCode
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from django.core.files.base import ContentFile
from django.conf import settings
from pathlib import Path
from pyzbar.pyzbar import decode
from PIL import Image
from pyzbar.pyzbar import decode
# from pyzbar import zbar_library
# Create QR code and save it


def generate_qr(request):
    qr_image_url = None
    error = None

    if request.method == 'POST':
        data = request.POST.get('qr_data')
        mobile_number = request.POST.get('mobile_number')

        # Mobile number validation
        if not mobile_number or len(mobile_number) != 10 or not mobile_number.isdigit():
            return render(request, 'scanner/generate.html', {
                'error': 'Invalid mobile number'
            })

        qr_content = f"{data}|{mobile_number}"
        qr = qrcode.make(qr_content)

        # Save QR to memory
        qr_image_io = BytesIO()
        qr.save(qr_image_io, format='PNG')
        qr_image_io.seek(0)

        # Set up file system path and storage
        qr_storage_path = settings.MEDIA_ROOT / 'qr_codes'
        fs = FileSystemStorage(location=qr_storage_path,
                               base_url='/media/qr_codes/')

        filename = f"{data}_{mobile_number}.png"
        qr_image_content = ContentFile(qr_image_io.read(), name=filename)

        # Save file and get URL
        file_path = fs.save(filename, qr_image_content)
        qr_image_url = fs.url(filename)

        # Save QR data to DB
        QRCode.objects.create(data=data, mobile_number=mobile_number)

    return render(request, 'scanner/generate.html', {
        'qr_image_url': qr_image_url,
        'error': error
    })


# Scan and validate QR code
def scan_qr(request):
    result = None

    if request.method == 'POST' and request.FILES.get('qr_image'):
        mobile_number = request.POST.get('mobile_number')
        qr_image = request.FILES['qr_image']

        # Mobile number validation
        if not mobile_number or len(mobile_number) != 10 or not mobile_number.isdigit():
            return render(request, 'scanner/scanner.html', {
                'error': 'Invalid mobile number'
            })

        # Save image temporarily
        fs = FileSystemStorage()
        filename = fs.save(qr_image.name, qr_image)
        image_path = Path(fs.location) / filename

        try:
            # Open and decode the image
            image_obj = Image.open(image_path)
            decoded_object = decode(image_obj)

            if not decoded_object:
                result = "No QR code found in the image."
            else:
                qr_content = decoded_object[0].data.decode('utf-8').strip()
                data_data, qr_mobile_number = qr_content.split('|')

                # Search for matching entry
                qr_entry = QRCode.objects.filter(
                    data=data_data, mobile_number=qr_mobile_number).first()

                if qr_entry and qr_mobile_number == mobile_number:
                    result = "Scan success: Valid QR Code for the provided mobile number."

                    # Delete from DB
                    qr_entry.delete()

                    # Delete QR image
                    qr_image_path = Path(
                        settings.MEDIA_ROOT) / 'qr_codes' / f"{data_data}_{qr_mobile_number}.png"
                    if qr_image_path.exists():
                        qr_image_path.unlink()

                else:
                    result = "QR code data doesn't match any record or mobile number mismatch."

        except Exception as e:
            result = f"Error processing the image: {str(e)}"

        finally:
            if image_path.exists():
                image_path.unlink()

    else:
        result = "No QR code detected in the image."

    return render(request, 'scanner/scanner.html', {'result': result})
